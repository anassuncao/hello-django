from django.db import models

# Create your models here.

# Para uma class nossa (neste caso a Item) ter as
# mesmas funcionalidades de classes existentes no
# Django temos de usar o inherit. A classe entre parêntesis
# é de onde queremos herdar as funcionalidades.


# This is a built in kind of field in Django that means
# this field will only have characters or text in it.
class Item(models.Model):
    # Entre parêntesis temos as restrições ao field.
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Esta função permite fazer um overwrite ao string method
    # by default do Django que define como o nome dos itens sao
    # mostrados na app.
    def __str__(self):
        return self.name
