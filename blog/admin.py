from django.contrib import admin
from .models import (AffiliateProgram, Category, Tag, InfoPost, ReviewPost,
					 TopMoneyPost, TopMoneyProduct, ReviewProduct, InfoProduct, AffiliateTag, TopMoneyLink, ReviewLink,
					 InfoLink)
from simple_history.admin import SimpleHistoryAdmin
# from guardian.admin import GuardedModelAdmin

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

# models_no_mixins = [AffiliateProgram, Category, Tag, InfoPost, ReviewPost, TopMoneyPost, TopMoneyProduct, ReviewProduct,
# 					InfoProduct, AffiliateTag, TopMoneyLink, ReviewLink, InfoLink, NormalLink,]

models_no_mixins_no_repeats = [AffiliateProgram, Category, Tag, TopMoneyPost, TopMoneyProduct, AffiliateTag, TopMoneyLink]

# admin.site.register(models_no_mixins, SimpleHistoryAdmin)
admin.site.register(models_no_mixins_no_repeats, SimpleHistoryAdmin)


# class AffiliateImageAdmin(GuardedModelAdmin):
# 	pass


# admin.site.register(AffiliateImage, AffiliateImageAdmin)
