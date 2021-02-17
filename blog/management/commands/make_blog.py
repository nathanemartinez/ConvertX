# from django.core.management.base import BaseCommand
# from django.utils import timezone
# from blog.models import (Category, Tag, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct, TopMoneyLink,
#                          PostMixin)
# from django.conf import settings
#
#
# class Command(BaseCommand):
#     help = 'Creates a dummy blog'
#     now = timezone.now()
#     User = settings.AUTH_USER_MODEL
#     u = User.objects.get(is_superuser=True, username='brickspy').first()
#
#     # def add_arguments(self, parser):
#     #     parser.add_argument('total', type=int, help='How many blog sets to create')
#     #     # parser.add_argument("-d", "--delay", type=int, help='')  # -d = command line, --deplay = in handle() method
#
#     @staticmethod
#     def get_name_mixin_fields():
#         fields = {
#             'name': 'default',
#             'description': 'descriptionnnn',
#         }
#         return fields
#
#     def get_timestamp_mixin_fields(self):
#         fields = {
#             'creator': self.u,
#             'updater': self.u,
#             'created_at': self.now,
#             'updated_at': self.now,
#         }
#         return fields
#
#     @staticmethod
#     def get_image_mixin_fields():
#         fields = {
#             'alt_tag': 'the alt of alt tags',
#             'caption': 'the caption',
#         }
#         return fields
#
#     @staticmethod
#     def get_ref_tag_mixin_fields(program: AffiliateProgram):
#         fields = {
#             'tag': 'default',
#             'program': program,
#         }
#         return fields
#
#     @staticmethod
#     def get_post_mixin_fields(category: Category, tag: Tag):
#         fields = {
#             'title': 'default',
#             'h1': 'h1 taggg',
#             'meta': 'metaaa',
#             'conclusion': "<p>I don't know if this is right</p>",
#             'category': category,
#             'tag': tag,
#             'year': 2021,
#             'status': PostMixin.DRAFT,
#         }
#         return fields
#
#     @staticmethod
#     def get_product_mixin_fields(program: AffiliateProgram):
#         fields = {
#             'title': 'default',
#             'content': '<p>content that is in a para tag</p>',
#             'sku': '123',
#             'price': 10,
#             'currency': 'USD',
#             'affiliate_program': program,
#             'available': True,
#         }
#         return fields
#
#     @staticmethod
#     def get_link_mixin_fields():
#         fields = {
#             'follow': TopMoneyLink.NO_FOLLOW,
#             'link': 'http://example.com',
#             'anchor_text': 'the text',
#         }
#         return fields
#
#     @staticmethod
#     def get_top_money_link_fields(tag: Tag, product: TopMoneyProduct):
#         fields = {
#             'tag': tag,
#             'product': product,
#         }
#         return fields
#
#     def handle(self, *args, **kwargs):
#         for i in range(2):
#             # Create category
#             my_kwargs = self.get_name_mixin_fields()
#             my_kwargs.update(self.get_timestamp_mixin_fields())
#             my_kwargs.update(self.get_image_mixin_fields())
#             category = Category.objects.create_category(**my_kwargs)
#             category.name = f'Category {category.pk}'
#             category.save()
#
#             # Create affiliate program
#             my_kwargs = self.get_name_mixin_fields()
#             my_kwargs.update(self.get_timestamp_mixin_fields())
#             program = AffiliateProgram.objects.create_affiliate_program(**my_kwargs)
#             program.name = f'Affiliate Program {program.pk}'
#             program.save()
#
#             # Create affiliate tag
#             my_kwargs = self.get_ref_tag_mixin_fields(program=program)
#             affiliate_tag = AffiliateTag.objects.create_tag(**my_kwargs)
#             affiliate_tag.tag = f'Affiliate Tag {affiliate_tag.pk}'
#             affiliate_tag.save()
#
#             for k in range(4):
#                 # Create tag
#                 my_kwargs = self.get_name_mixin_fields()
#                 my_kwargs.update(self.get_timestamp_mixin_fields())
#                 tag = Tag.objects.create_tag(**my_kwargs)
#                 tag.name = f'Tag {tag.pk}'
#                 tag.save()
#
#                 for j in range(2):
#                     # Create top money post
#                     my_kwargs = self.get_post_mixin_fields(category, tag)
#                     my_kwargs.update(self.get_timestamp_mixin_fields())
#                     my_kwargs.update(self.get_image_mixin_fields())
#                     post = TopMoneyPost.objects.create_post(**my_kwargs)
#                     post.title = f'Post {post.pk}'
#                     post.save()
#
#                     for f in range(5):
#                         # Create top money product
#                         my_kwargs = self.get_product_mixin_fields(program)
#                         my_kwargs.update(self.get_timestamp_mixin_fields())
#                         my_kwargs.update(self.get_image_mixin_fields())
#                         product = TopMoneyProduct.objects.create_product(**my_kwargs)
#                         product.title = f'Product {product.pk}'
#                         product.save()
#
#                         # Create top money link
#                         my_kwargs = self.get_link_mixin_fields()
#                         my_kwargs.update(self.get_top_money_link_fields(tag, product))
#                         my_kwargs.update(self.get_timestamp_mixin_fields())
#                         link = TopMoneyLink.objects.create_link(**my_kwargs)
#                         link.anchor_text = f'Link {link.pk}'
#                         link.save()
#
#
#
#
#
#
