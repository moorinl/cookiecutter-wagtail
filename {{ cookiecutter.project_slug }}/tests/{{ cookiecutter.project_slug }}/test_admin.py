import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_admin_is_available(client):
    res = client.get(reverse('admin:index'), follow=True)
    assert res.status_code == 200
