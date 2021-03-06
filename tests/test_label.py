from yandex_music import Label


class TestLabel:
    id = 148217
    name = 'tommee profitt STUDIOS'

    def test_expected_values(self, label):
        assert label.id == self.id
        assert label.name == self.name

    def test_de_json_required(self, client):
        json_dict = {'id': self.id, 'name': self.name}
        label = Label.de_json(json_dict, client)

        assert label.id == self.id
        assert label.name == self.name

    def test_de_json_all(self, client):
        json_dict = {'id': self.id, 'name': self.name}
        label = Label.de_json(json_dict, client)

        assert label.id == self.id
        assert label.name == self.name

    def test_equality(self):
        a = Label(self.id, self.name)
        b = Label(10, self.name)
        c = Label(self.id, '')
        d = Label(self.id, self.name)

        assert a != b != c
        assert hash(a) != hash(b) != hash(c)
        assert a is not b is not c

        assert a == d
