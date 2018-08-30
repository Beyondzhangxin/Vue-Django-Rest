def getSamples(gmmConfig):
    switch = {
        "SPGS": DataSpgsHistory,
        "PVMG": DataPvmgHistory,
    }
    start = datetime.datetime.strptime(gmmConfig.start_time, "%Y-%m-%dT%H:%M:%S.%ZZ")
    end = datetime.datetime.strptime(gmmConfig.end_time, "%Y-%m-%dT%H:%M:%S.%ZZ")
    response = {}
    try:
        samples = switch[gmmConfig.system].objects.filter(datatime_range=(start,end)).values_list(json.loads(gmmConfig.varables), flat=True)
        return samples
    except Exception as e:
        return []