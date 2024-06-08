from django.db import models

class Ctenar(models.Model):
    uzivatelske_jmeno = models.CharField(max_length=80, verbose_name='Uživatelské jméno', help_text='Zadejte uživatelské jméno',
                                         error_messages={'blank': 'Uživatelské jméno musí být vyplněno'})
    email = models.EmailField(verbose_name='Emailová adresa', help_text='Zadejte emailovou adresu',
                              error_messages={'blank': 'Emailová adresa musí být vyplněna'})
    datum_registrace = models.DateField(auto_now_add=True, verbose_name='Datum registrace')
    aktivni = models.BooleanField(default=True, verbose_name='Aktivní účet')

    class Meta:
        ordering = ['uzivatelske_jmeno']
        verbose_name = 'Čtenář'
        verbose_name_plural = 'Čtenáři'

    def __str__(self):
        return self.uzivatelske_jmeno


class Pujcka(models.Model):
    ctenar = models.ForeignKey('projektapp.Ctenar', on_delete=models.CASCADE, verbose_name='Čtenář')
    datum_pujceni = models.DateField(auto_now_add=True, verbose_name='Datum půjčení')
    datum_vraceni = models.DateField(blank=True, null=True, verbose_name='Datum vrácení')

    class Meta:
        ordering = ['datum_pujceni']
        verbose_name = 'Půjčka'
        verbose_name_plural = 'Půjčky'

    def __str__(self):
        return f'Půjčka pro {self.ctenar}'


class Knihovna(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název knihovny', help_text='Zadejte název knihovny',
                             error_messages={'blank': 'Název knihovny je povinný údaj'})
    adresa = models.CharField(max_length=200, verbose_name='Adresa knihovny', help_text='Zadejte adresu knihovny',
                              error_messages={'blank': 'Adresa knihovny je povinný údaj'})
    telefon = models.CharField(max_length=15, verbose_name='Telefonní číslo', help_text='Zadejte telefonní číslo knihovny')
    email = models.EmailField(verbose_name='Email knihovny', help_text='Zadejte emailovou adresu knihovny')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Knihovna'
        verbose_name_plural = 'Knihovny'

    def __str__(self):
        return self.nazev


class Knihovnik(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno knihovníka', help_text='Zadejte jméno knihovníka',
                             error_messages={'blank': 'Jméno knihovníka musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení knihovníka', help_text='Zadejte příjmení knihovníka',
                                error_messages={'blank': 'Příjmení knihovníka musí být vyplněno'})
    knihovna = models.ForeignKey('Knihovna', on_delete=models.CASCADE, verbose_name='Knihovna')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Knihovník'
        verbose_name_plural = 'Knihovníci'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Rezervace(models.Model):
    ctenar = models.ForeignKey('projektapp.Ctenar', on_delete=models.CASCADE, verbose_name='Čtenář')
    datum_rezervace = models.DateField(auto_now_add=True, verbose_name='Datum rezervace')
    stav = models.CharField(max_length=20, choices=[('cekajici', 'Čekající'), ('vyzvednuto', 'Vyzvednuto')],
                            default='cekajici', verbose_name='Stav rezervace')

    class Meta:
        ordering = ['datum_rezervace']
        verbose_name = 'Rezervace'
        verbose_name_plural = 'Rezervace'

    def __str__(self):
        return f'Rezervace pro {self.ctenar} - {self.stav}'
