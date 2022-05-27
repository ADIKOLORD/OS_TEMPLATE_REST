from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from .models import MyModel, Category, Cart, MyUser
from django.db.models import QuerySet

admin.site.register(MyUser)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class MyModelAdmin(admin.ModelAdmin):
    # Отображение на экране
    list_display = ['title', 'price', 'category', 'get_html_photo']

    # Редоктирование прямо в панеле
    list_editable = ['price', 'category']

    # Кайсыларды басканда кириш керек ошол объектке
    list_display_links = ['title', ]

    # Бир страницада канча запись болуш керек
    list_per_page = 3

    # fields -> Кайсы поляларды толтурганга болот. Же добавить эткенде кайсылар корунсун
    # fields = []

    # readonly_fields -> Кайсыларды изменить этсе болбойт!
    readonly_fields = []

    # Создать или редоктировать эткенде корунбогондор
    exclude = ['pub_date', 'update_date']

    # Фильтр для сортировки
    list_filter = ['category', ]

    # Поиск
    search_fields = ['title', 'description']

    # Вертикальное и Горизантальное отображение ManyToManyField
    filter_vertical = ['cart']

    # filter_horizontal = ['cart']

    # save_on_top = True  # for show button 'save' in top

    # save_as = True  # Если бар моделька болсо сох. эткенде новый болот

    # actions_on_bottom = True  # Понятно эле го дейм атынан эле 🙃
    # actions_on_top = False

    # date_hierarchy -> Админ панелде дата менен сортировка кылганы
    date_hierarchy = 'pub_date'

    actions_selection_counter = False

    def get_html_photo(self, object):
        '''
        Отображает фото вместо ссылки
        '''
        if object.image:
            '''
            mark_safe -> didn't ignore html code
            '''
            return mark_safe(f"<img src='{object.image.url}' style='width:50px;height:50px;'")

    get_html_photo.short_description = 'Фото моделки'

    # actions -> Кайсы дествиялар болуш керек
    actions = [
        'set_clone_model',
        'set_status_old',
    ]

    # Добавление дествии
    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()

    @admin.action(description='SET STATUS OLD')
    def set_status_old(self, request, qs: QuerySet):
        for object in qs:
            object.status = 'OLD'
            object.save()

    """
    @admin.action(description='Установить категорию Sport')
    def set_category_sport(self, request, qs: QuerySet):
        count_updates = qs.update(category=3)
        # self.message_user -> Функция болгондо кандай сообщение чыгарына жооп берет.
        self.message_user(request,
                          f'Было обновлено {count_updates} записей',
                          # level -> INFO Записьти жашыл кылат, ERROR кызыл
                          level=messages.INFO
                          )

    @admin.action(description='Установить категорию Man')
    def set_category_man(self, request, qs: QuerySet):
        qs.update(category=1)

    @admin.action(description='Установить категорию Woman')
    def set_category_woman(self, request, qs: QuerySet):
        qs.update(category=2)

    @admin.action(description='Установить категорию Electric')
    def set_category_electric(self, request, qs: QuerySet):
        qs.update(category=4)

    
    """


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Cart)
