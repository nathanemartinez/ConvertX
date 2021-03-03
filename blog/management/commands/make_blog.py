from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import (Category, SubCategory, AffiliateProgram, AffiliateTag, TopMoneyPost, TopMoneyProduct, TopMoneyLink,
                         PostMixin)
from blog.constants import user
from django.utils.text import slugify
from temp import text

class Command(BaseCommand):
    """
    Creates a dummy blog
    """
    help = 'Creates a dummy blog'
    now = timezone.now()
    u = user

    # def add_arguments(self, parser):
    #     parser.add_argument('total', type=int, help='How many blog sets to create')
    #     # parser.add_argument("-d", "--delay", type=int, help='')  # -d = command line, --deplay = in handle() method

    @staticmethod
    def get_name_mixin_fields():
        fields = {
            'name': 'default',
            'description': 'descriptionnnn',
        }
        return fields

    def get_timestamp_mixin_fields(self):
        fields = {
            'creator': self.u,
            'updater': self.u,
            'created_at': self.now,
            'updated_at': self.now,
        }
        return fields

    @staticmethod
    def get_image_mixin_fields():
        fields = {
            'alt_tag': 'the alt of alt tags',
            'caption': 'the caption',
        }
        return fields

    @staticmethod
    def get_ref_tag_mixin_fields(program: AffiliateProgram):
        fields = {
            'tag': 'default',
            'program': program,
        }
        return fields

    @staticmethod
    def get_post_mixin_fields():
        fields = {
            'title': 'default',
            'h1': 'h1 taggg',
            'meta': 'metaaa',
            'year': 2021,
            'status': PostMixin.DRAFT,
        }
        return fields

    @staticmethod
    def get_product_mixin_fields():
        fields = {
            'title': 'default',
            'content': '<p>content that is in a para tag</p>',
            'sku': '123',
            'price': 10,
            'currency': 'USD',
            'available': True,
        }
        return fields

    @staticmethod
    def get_link_mixin_fields():
        fields = {
            'follow': TopMoneyLink.NO_FOLLOW,
            'link': 'http://example.com',
            'anchor_text': 'the text',
        }
        return fields

    @staticmethod
    def get_top_money_link_fields(tag, product):
        fields = {
            'tag': tag,
            'product': product,
        }
        return fields

    def handle(self, *args, **kwargs):
        counter1 = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0
        for i in range(2):
            counter1 += 1
            # Create category
            my_kwargs = self.get_name_mixin_fields()
            my_kwargs.update(self.get_timestamp_mixin_fields())
            my_kwargs.update(self.get_image_mixin_fields())
            category = Category.objects.create_category(**my_kwargs)
            category.name = f'Category {counter1}'
            category.save()

            # Create affiliate program
            my_kwargs = self.get_name_mixin_fields()
            my_kwargs.update(self.get_timestamp_mixin_fields())
            program = AffiliateProgram.objects.create_affiliate_program(**my_kwargs)
            program.name = f'Affiliate Program {counter1}'
            program.save()

            # Create affiliate tag
            my_kwargs = self.get_ref_tag_mixin_fields(program=program)
            affiliate_tag = AffiliateTag.objects.create_tag(**my_kwargs)
            affiliate_tag.tag = f'Affiliate Tag {counter1}'
            affiliate_tag.save()

            for k in range(2):
                counter2 += 1
                # Create tag
                # my_kwargs = self.get_name_mixin_fields()
                # my_kwargs.update(self.get_timestamp_mixin_fields())
                # tag = Tag.objects.create_tag(**my_kwargs)
                # tag.name = f'Tag {counter2}'
                # tag.save()

                # Subcategory
                my_kwargs = self.get_name_mixin_fields()
                my_kwargs.update(self.get_timestamp_mixin_fields())
                my_kwargs.update(self.get_timestamp_mixin_fields())
                subcategory = SubCategory.objects.create_subcategory(**my_kwargs)
                subcategory.name = f'Sub Category {counter2}'
                subcategory.category = category
                subcategory.save()

                for j in range(3):
                    counter3 += 1
                    # Create top money post
                    my_kwargs = self.get_post_mixin_fields()
                    my_kwargs.update(self.get_timestamp_mixin_fields())
                    my_kwargs.update(self.get_image_mixin_fields())
                    post = TopMoneyPost.objects.create_post(**my_kwargs)
                    post.title = f'Post lawl lawl test {counter3}'
                    post.slug = slugify(post.title)
                    post.subcategory = subcategory
                    post.intro = text.intro
                    post.conclusion = text.conclusion
                    # post.tag.add(tag)
                    post.save()

                    for f in range(2):
                        counter4 += 1
                        # Create top money product
                        my_kwargs = self.get_product_mixin_fields()
                        my_kwargs.update(self.get_timestamp_mixin_fields())
                        my_kwargs.update(self.get_image_mixin_fields())
                        product = TopMoneyProduct.objects.create_product(**my_kwargs)
                        product.title = f'Post {counter4}'
                        product.post = post
                        product.save()

                        # Create top money link
                        my_kwargs = self.get_link_mixin_fields()
                        my_kwargs.update(self.get_top_money_link_fields(affiliate_tag, product))
                        my_kwargs.update(self.get_timestamp_mixin_fields())
                        link = TopMoneyLink.objects.create_link(**my_kwargs)
                        link.anchor_text = f'Link {counter4}'
                        link.save()

