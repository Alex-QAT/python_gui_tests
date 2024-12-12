
def test_del_group(app):
    old_gr_list = app.groups.get_gr_list()
    if len(old_gr_list) == 1:
        app.groups.add_new_gr("my group")
        old_gr_list = app.groups.get_gr_list()
    app.groups.del_gr()
    new_gr_list = app.groups.get_gr_list()
    new_gr_list.append("my group")
    assert sorted(old_gr_list) == sorted(new_gr_list)