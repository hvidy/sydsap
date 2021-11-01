import lightkurve as lk
from scipy.ndimage import binary_dilation
import numpy as np

class sydsap_tpf(lk.TessTargetPixelFile):

	def sydsap(self,mask=None,threshold=3,dilation=1):

		if mask == None:
			# Create new mask to use for simple aperture photometry
			mask = self.create_threshold_mask(threshold=threshold)
			# Dilate mask to minimise aperture losses due to pointing jitter
			if dilation > 0:
				mask = binary_dilation(mask,iterations=dilation)

		# Generate raw light curve
		lc = self.to_lightcurve(aperture_mask = mask)

		#
		# Use regression corrector to improve light curve
		#
		
		# Indentify NaN pixels
		nanpixels = np.isnan(np.nanmean(self.flux,axis=0))

		# Pixels that are neither in aperture mask or nan
		outpixels = ~nanpixels & ~mask

		# Make regressors from outer pixels
		regressors = self.flux[:,outpixels]

		# Identify time steps where flux error is NaN
		nantimes = np.isnan(lc.flux_err)

		# Only include time steps where flux error is ~Nan in regressors
		regressors = regressors[~nantimes,:]

		# Make design matrix from our regressors, taking 5 principal components, adding a constant
		dm = lk.DesignMatrix(regressors, name = 'regressors').pca(5).append_constant()

		# Make corrector object
		corrector = lk.RegressionCorrector(lc[~nantimes])

		# Correct light curve
		lc = corrector.correct(dm)

		# Return lc
		return lc