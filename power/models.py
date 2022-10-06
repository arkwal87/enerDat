from django.db import models
import pandas as pd


# Create your models here.

class FiveYearPlan(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=3)
    grid_demand_forecast = models.IntegerField()
    required_power_reserve = models.IntegerField()
    surplus_capacity = models.IntegerField()
    available_capacity = models.IntegerField()
    available_capacity_for_tso = models.IntegerField()
    cent_dispatched_units_gen_forecast = models.IntegerField()
    non_cent_dispatched_units_gen_forecast = models.IntegerField()
    wind_gen_forecast = models.IntegerField()
    pv_gen_forecast = models.IntegerField()
    planned_cross_border_exchange = models.IntegerField()
    network_losses_forecast = models.IntegerField()
    capacity_market_obligation = models.IntegerField()
    download_date = models.IntegerField()

    def add_to_model(self):
        df = pd.read_csv(
            'https://www.pse.pl/getcsv/-/export/csv/EN_PD_GO_BILANS/data_od/20221003/data_do/20221004',
            delimiter=";",
            encoding="unicode_escape",
            nrows=24)
        model_instances = [FiveYearPlan()]
        FiveYearPlan.objects.bulk_create(model_instances)