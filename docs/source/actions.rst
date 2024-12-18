Команды окна
============

.. _aspect_actions:

Команды текущего аспекта [1а]
-----------------------------

* ``Перефильтровать`` — очистить и заполнить дерево объектов;
* ``Записать свойства объектов`` — записать коды в свойства объектов и сохранить дерево объектов.

При первом открытии окна BIM Classifier происходит заполнение дерева объектов по правилам JSON-схемы, указанной в параметре аспекта ``Json схема для создания групп``. При нажатии на команду ``Перефильтровать`` происходит очистка и заполнение дерева объектов, но с сохранением введенных данных. С помощью этой команды можно обновить дерево объектов аспекта после изменений в ЦИМ Renga.

Обе команды выполняют длительные операции. Время выполнения зависит от количества объектов ЦИМ Renga.

.. note::

    После сохранения состояния дерева объектов команда ``Перефильтровать`` выполняется значительно быстрее, чем первое построение дерева объектов во время первого запуска BIM Classifier.

Можно сохранить состояние системы кодового обозначения и закрыть окно BIM Classifier. А затем продолжить работу с последнего сохраненного состояния. Данные системы кодового обозначения сохраняются в проект Renga.

.. _parameters_actions:

Команды панели параметров аспекта [2а]
--------------------------------------

* ``Скрыть-показать параметры`` — скрыть/показать панель параметров аспекта.

.. _aspects_actions:

Команды аспектов [3]
--------------------

* ``Дублировать`` — дублировать текущий аспект;
* ``Очистить`` — очистить текущий аспект от введенных данных;
* ``Удалить`` — удалить текущий аспект.

.. note::

    Аспекты, заданные по умолчанию, удалить нельзя.

Команды окна BIM Classifier [4]
-------------------------------

* ``Сохранить`` — сохранить текущее состояние системы кодового обозначения и выйти из BIM Classifier;
* ``Отмена`` — выйти из BIM Classifier без сохранения введенных данных.

.. important::

    Сохранение системы кодового обозначения производится в свойство **Проекта** ``ClassifierData`` ЦИМ Renga в закодированном виде. Если очистить значение этого свойства, то состояние системы кодового обозначения сбросится на первоначальное состояние.