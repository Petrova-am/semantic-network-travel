# nodes.py
nodes = {
    # Классы
    "cls_country": {"type": "class", "name": "Страна"},
    "cls_beach_country": {"type": "class", "name": "Пляжная страна"},
    "cls_cultural_country": {"type": "class", "name": "Культурная страна"},
    "cls_exotic_country": {"type": "class", "name": "Экзотическая страна"},
    "cls_season": {"type": "class", "name": "Сезон"},
    "cls_interest": {"type": "class", "name": "Интерес"},
    "cls_visa": {"type": "class", "name": "Визовый режим"},
    "cls_transport": {"type": "class", "name": "Транспортная доступность"},
    # Экземпляры стран
    "inst_turkey": {"type": "instance", "name": "Турция", "class": "cls_beach_country"},
    "inst_china": {"type": "instance", "name": "Китай", "class": "cls_cultural_country"},
    "inst_vietnam": {"type": "instance", "name": "Вьетнам", "class": "cls_exotic_country"},
    "inst_egypt": {"type": "instance", "name": "Египет", "class": "cls_beach_country"},
    "inst_thailand": {"type": "instance", "name": "Таиланд", "class": "cls_beach_country"},
    # Сезоны
    "inst_spring": {"type": "instance", "name": "Весна", "class": "cls_season"},
    "inst_summer": {"type": "instance", "name": "Лето", "class": "cls_season"},
    "inst_autumn": {"type": "instance", "name": "Осень", "class": "cls_season"},
    "inst_winter": {"type": "instance", "name": "Зима", "class": "cls_season"},
    # Интересы
    "inst_beach": {"type": "instance", "name": "Пляж", "class": "cls_interest"},
    "inst_culture": {"type": "instance", "name": "Культура", "class": "cls_interest"},
    "inst_nature": {"type": "instance", "name": "Природа", "class": "cls_interest"},
    "inst_exotic": {"type": "instance", "name": "Экзотика", "class": "cls_interest"},
    # Визы
    "inst_visa_free": {"type": "instance", "name": "Безвизовый", "class": "cls_visa"},
    "inst_visa_on_arrival": {"type": "instance", "name": "Виза по прибытии", "class": "cls_visa"},
    # Транспорт
    "inst_direct_flight": {"type": "instance", "name": "Прямой рейс", "class": "cls_transport"},
    # Значения
    "val_days_60": {"type": "value", "name": "60 дней"},
    "val_days_30": {"type": "value", "name": "30 дней"},
    "val_days_45": {"type": "value", "name": "45 дней"},
    "val_usd_30": {"type": "value", "name": "30 USD"},
}