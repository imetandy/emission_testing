class Emitter:
    def __init__(self):
        self.sst = 21
        self.ec_distribution_pct = 0.05
        self.gc_distribution_pct = 0.05
        self.daily_ec_total = 1000
        self.daily_gc_total = 1000

    def fetch_sst(self):
        """Placeholder for fetching the daily SST value."""
        return self.sst

    def calculate_ec(self):
        """Placeholder for calculating daily EC emission."""
        return self.daily_ec_total

    def calculate_gc(self):
        """Placeholder for calculating daily GC emission."""
        return self.daily_gc_total

    def climate_fund(self):
        """Placeholder for calculating the climate fund."""
        return (self.daily_ec_total*self.ec_distribution_pct) + (self.daily_gc_total*self.gc_distribution_pct)

    def distribute_ec(self):
        """Distribute daily EC emission to the traders."""
        return self.daily_ec_total * self.ec_distribution_pct

    def distribute_gc(self):
        """Distribute daily GC emission to the traders."""
        return self.daily_gc_total * self.gc_distribution_pct

    def emit(self):
        """Emit daily EC and GC."""
        self.fetch_sst()
        self.calculate_ec()
        self.calculate_gc()
        return self.distribute_ec(), self.distribute_gc()

        # Do traders receive EC and GC ??


