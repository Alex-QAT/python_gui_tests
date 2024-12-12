class GroupHelper:
    def __init__(self,app):
        self.app = app

    def get_gr_list(self):
        self.open_gr_editor()
        tree = self.gr_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        gr_list = [node.text() for node in root.children()]
        self.close_gr_editor()
        return gr_list

    def add_new_gr(self, name):
        self.open_gr_editor()
        self.gr_editor.window(auto_id="uxNewAddressButton").click()
        input = self.gr_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_gr_editor()

    def del_gr(self):
        self.open_gr_editor()
        # нашли дерево списка
        tree = self.gr_editor.window(auto_id="uxAddressTreeView")
        # нашли корень дерева списка
        root = tree.tree_root()
        # берём первый элемент из списка детей этого корня (первый потому что нумерация с нулевого а нулевой он дефолтный, он всегда присутствует и его удалить нельзя)
        group = root.children()[1]
        # кликаем по этому элементу (группе)
        group.click()
        # жмём кнопку Delete в окне Group editor
        self.gr_editor.window(auto_id="uxDeleteAddressButton").click()
        # находим следующее окно для подтверждения удаления Delete Group
        self.del_gr_submit = self.app.application.window(title="Delete group")
        self.del_gr_submit.wait("visible")
        # жмём Ок
        self.del_gr_submit.window(auto_id="uxOKAddressButton").click()
        #Закрываем окно Group editor
        self.close_gr_editor()


    def open_gr_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.gr_editor = self.app.application.window(title="Group editor")
        self.gr_editor.wait("visible")


    def close_gr_editor(self):
        self.gr_editor.close()
