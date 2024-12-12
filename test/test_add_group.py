
def test_add_group(app):
    old_gr_list = app.groups.get_gr_list()
    app.groups.add_new_gr("my group")
    new_gr_list = app.groups.get_gr_list()
    old_gr_list.append("my group")
    assert sorted(old_gr_list) == sorted(new_gr_list)