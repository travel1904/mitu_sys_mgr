import math


def owner_page(request, obj):
    """
    # 自定义分页器
    :param request: request请求
    :param obj: 分页对象
    :return: 所在页码的对象集，所有页码，当前页码，分页对象的总数
    """
    current_page = 1
    all_page = 1
    page_type = ''
    try:
        current_page = int(request.GET.get('cur', '1'))
        all_page = int(request.GET.get('all', '1'))
        page_type = str(request.GET.get('action', ''))  # 向前翻页还是向下翻页
    except ValueError:
        current_page = 1
        all_page = 1
        page_type = ''

    if page_type == 'next':
        current_page += 1
    elif page_type == 'previous':
        current_page -= 1
    if isinstance(obj, list):
        count = len(obj)
    else:
        count = obj.count()
    # print(current_page)
    # print(obj)
    start = (current_page - 1) * 10
    end = current_page * 10
    data = obj[start:end]
    # print(data)

    if current_page == 1 and current_page == 1:  # 标记1
        all_page = math.ceil(count / 10)
    return data, all_page, current_page, count