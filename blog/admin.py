from django.contrib import admin
from .models import (AffiliateImage, AffiliateLink, AffiliateProduct, AffiliateProgram, Category, InfoPost,
					 InfoPostEstimates, NormalImage, NormalLink, ReviewPost, ReviewPostEstimates, Tag, TopMoneyPost,
					 TopMoneyPostEstimates,)
from simple_history.admin import SimpleHistoryAdmin
from guardian.admin import GuardedModelAdmin

# from .models import (AffiliateImage, AffiliateLink, AffiliateProduct, AffiliateProgram, Category, ImageMixin, InfoPost,
# 					 InfoPostEstimates, LinkMixin, NameMixin, NormalImage, NormalLink, PostEstimatesMixin, PostMixin,
# 					 ProductMixin, ReviewPost, ReviewPostEstimates, Tag, TimeStampCreatorMixin, TopMoneyPost,
# 					 TopMoneyPostEstimates,)

# models_with_mixins = [AffiliateImage, AffiliateLink, AffiliateProduct, AffiliateProgram, Category, ImageMixin, InfoPost,
# 						InfoPostEstimates, LinkMixin, NameMixin, NormalImage, NormalLink, PostEstimatesMixin, PostMixin,
# 						ProductMixin, ReviewPost, ReviewPostEstimates, Tag, TimeStampCreatorMixin, TopMoneyPost,
# 						TopMoneyPostEstimates,]
#
# admin.site.register(models_with_mixins)

models_no_mixins = [AffiliateImage, AffiliateLink, AffiliateProduct, AffiliateProgram, Category, InfoPost,
					InfoPostEstimates, NormalImage, NormalLink, ReviewPost, ReviewPostEstimates, Tag, TopMoneyPost,
					TopMoneyPostEstimates,]

admin.site.register(models_no_mixins, SimpleHistoryAdmin)


# class AffiliateImageAdmin(GuardedModelAdmin):
# 	pass


# admin.site.register(AffiliateImage, AffiliateImageAdmin)
