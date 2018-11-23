from django.contrib.gis.db import models


class EditableModel(models.Model):
    gid = models.AutoField(primary_key=True)
    campo1 = models.CharField(max_length=100, blank=True, null=True)
    campo2 = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        db_table = 'editable_model'


class ActividadesAgropecuarias(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=110, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actividades_agropecuarias'


class ActividadesEconomicas(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=61, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actividades_economicas'


class ComplejoDeEnergiaEne(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=75, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'complejo_de_energia_ene'


class CursoDeAguaHid(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=77, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cuenca = models.CharField(max_length=50, blank=True, null=True)
    contenido = models.CharField(max_length=50, blank=True, null=True)
    coincide = models.CharField(max_length=39, blank=True, null=True)
    navegable = models.CharField(max_length=33, blank=True, null=True)
    profundida = models.CharField(max_length=33, blank=True, null=True)
    régimen = models.CharField(max_length=29, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.CharField(max_length=30, blank=True, null=True)
    igds_weigh = models.CharField(max_length=30, blank=True, null=True)
    rotation = models.CharField(max_length=30, blank=True, null=True)
    igds_color = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)
    igds_level = models.CharField(max_length=30, blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'curso_de_agua_hid'


class CurvasDeNivel(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=59, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cota = models.CharField(max_length=61, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    corregidas = models.IntegerField(blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'curvas_de_nivel'


class EdifConstruccionesTuristicas(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=43, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=254, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edif_construcciones_turisticas'


class EdifDeporYEsparcimiento(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=91, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edif_depor_y_esparcimiento'


class EdifEducacion(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=39, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edif_educacion'


class EdifReligiosos(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=73, blank=True, null=True)
    religión = models.CharField(max_length=29, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edif_religiosos'


class EdificioDeSaludIps(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=143, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edificio_de_salud_ips'


class EdificioDeSeguridadIps(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=175, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edificio_de_seguridad_ips'


class EdificioPublicoIps(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=79, blank=True, null=True)
    precisión = models.CharField(max_length=8, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edificio_publico_ips'


class EdificiosFerroviarios(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=68, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    opeador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=254, blank=True, null=True)
    fclass = models.CharField(max_length=254, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    admin = models.CharField(max_length=51, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'edificios_ferroviarios'


class Ejido(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=73, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    esc = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    departamen = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=70, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    coddepto = models.CharField(max_length=6, blank=True, null=True)
    codloc = models.CharField(max_length=6, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ejido'


class EspejoDeAguaHid(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=98, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cuenca = models.CharField(max_length=100, blank=True, null=True)
    uso = models.CharField(max_length=29, blank=True, null=True)
    salinidad = models.CharField(max_length=2, blank=True, null=True)
    régimen = models.CharField(max_length=29, blank=True, null=True)
    navegabili = models.CharField(max_length=33, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'espejo_de_agua_hid'


class EstructurasPortuarias(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=151, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'estructuras_portuarias'


class InfraestructuraAeroportuariaPunto(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=194, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    uso = models.CharField(max_length=43, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'infraestructura_aeroportuaria_punto'


class InfraestructuraHidro(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=145, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'infraestructura_hidro'


class Isla(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=64, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'isla'


class LimitePoliticoAdministrativoLim(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=188, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    extensión = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    claselim = models.CharField(max_length=51, blank=True, null=True)
    aclaracion = models.CharField(max_length=200, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'limite_politico_administrativo_lim'


class Localidades(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=73, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=77, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    provincia = models.CharField(max_length=70, blank=True, null=True)
    departamen = models.CharField(max_length=50, blank=True, null=True)
    coddepto = models.CharField(max_length=6, blank=True, null=True)
    codloc = models.CharField(max_length=6, blank=True, null=True)
    canthab = models.FloatField(blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'localidades'


class LineasDeConduccionEne(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=143, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    consesión = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=50, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'líneas_de_conducción_ene'


class MarcasYSenales(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=55, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cota = models.CharField(max_length=29, blank=True, null=True)
    red = models.CharField(max_length=41, blank=True, null=True)
    monografía = models.CharField(max_length=30, blank=True, null=True)
    x_inch = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    y_inch = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    lat_inch = models.CharField(max_length=30, blank=True, null=True)
    long_inch = models.CharField(max_length=30, blank=True, null=True)
    x_posgar = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    y_posgar = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    lat_posgar = models.CharField(max_length=30, blank=True, null=True)
    posgar = models.CharField(max_length=30, blank=True, null=True)
    fotomonogr = models.CharField(max_length=38, blank=True, null=True)
    malla = models.CharField(max_length=3, blank=True, null=True)
    número = models.CharField(max_length=5, blank=True, null=True)
    en_uso = models.CharField(max_length=3, blank=True, null=True)
    orden = models.CharField(max_length=3, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    cotbase = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'marcas_y_señales'


class MuroEmbalse(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=78, blank=True, null=True)
    situacion = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'muro_embalse'


class ObraDeComunicacion(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=76, blank=True, null=True)
    precision = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'obra_de_comunicación'


class ObraPortuaria(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    precisión = models.CharField(max_length=60, blank=True, null=True)
    escala = models.CharField(max_length=70, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    material = models.CharField(max_length=254, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'obra_portuaria'


class OtrasEdificaciones(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=80, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=254, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'otras_edificaciones'


class PaisLim(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    sigla = models.CharField(max_length=5, blank=True, null=True)
    población = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    # Field name made lowercase.
    área_of = models.DecimalField(
        db_column='Área_of', max_digits=65535, decimal_places=65535, blank=True, null=True)
    moneda_of = models.CharField(max_length=50, blank=True, null=True)
    idioma_of = models.CharField(max_length=50, blank=True, null=True)
    continente = models.CharField(max_length=50, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pais_lim'


class Provincias(models.Model):
    gid = models.AutoField(primary_key=True)
    # Field renamed because it contained more than one '_' in a row.
    # Field renamed because it started with '_'.
    field_gid = models.DecimalField(
        db_column='__gid', max_digits=10, decimal_places=0,
        blank=True, null=True)
    prov = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'provincias'


class PuenteRedVialPuntos(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    situación = models.CharField(max_length=70, blank=True, null=True)
    precision = models.CharField(max_length=60, blank=True, null=True)
    escala = models.CharField(max_length=60, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=70, blank=True, null=True)
    fclass = models.CharField(max_length=70, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    sist_uso = models.CharField(max_length=60, blank=True, null=True)
    material = models.CharField(max_length=60, blank=True, null=True)
    libre_hz = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    libre_vcal = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    capacidad = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    carriles = models.CharField(max_length=254, blank=True, null=True)
    largo = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'puente_red_vial_puntos'


class PuntosDeAlturasTopograficas(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    precisión = models.CharField(max_length=254, blank=True, null=True)
    escala = models.CharField(max_length=254, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=254, blank=True, null=True)
    fclass = models.CharField(max_length=254, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cota = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    cotbase = models.FloatField(blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'puntos_de_alturas_topograficas'


class PuntosDelTerreno(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    precisión = models.CharField(max_length=70, blank=True, null=True)
    escala = models.CharField(max_length=60, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=70, blank=True, null=True)
    fclass = models.CharField(max_length=70, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cota = models.CharField(max_length=50, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    cotbase = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'puntos_del_terreno'


class RedFerroviaria(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisíon = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    clase = models.CharField(max_length=29, blank=True, null=True)
    lin_ferr = models.CharField(max_length=99, blank=True, null=True)
    trocha = models.CharField(max_length=34, blank=True, null=True)
    electrific = models.CharField(max_length=29, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    max_carg = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    actualizac = models.CharField(max_length=50, blank=True, null=True)
    concesión = models.CharField(max_length=29, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'red_ferroviaria'


class RedVial(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=228, blank=True, null=True)
    situación = models.CharField(max_length=36, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    administra = models.CharField(max_length=51, blank=True, null=True)
    revestimie = models.CharField(max_length=29, blank=True, null=True)
    carriles = models.CharField(max_length=31, blank=True, null=True)
    tráfico = models.CharField(max_length=29, blank=True, null=True)
    cante_div = models.CharField(max_length=32, blank=True, null=True)
    de_carga = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    km_inicial = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    nro_ruta = models.CharField(max_length=15, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    categoría = models.CharField(max_length=29, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'red_vial'


class SalvadoDeObstaculo(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    precision = models.CharField(max_length=60, blank=True, null=True)
    escala = models.CharField(max_length=60, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=70, blank=True, null=True)
    fclass = models.CharField(max_length=70, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'salvado_de_obstaculo'


class Senalizaciones(models.Model):
    gid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    situacion = models.CharField(max_length=50, blank=True, null=True)
    precision = models.CharField(max_length=50, blank=True, null=True)
    escala = models.CharField(max_length=254, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=60, blank=True, null=True)
    fclass = models.CharField(max_length=60, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    cell_name = models.CharField(max_length=8, blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'señalizaciones'


class SueCongelado(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=190, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sue_congelado'


class SueConsolidado(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=139, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.CharField(max_length=30, blank=True, null=True)
    igds_weigh = models.CharField(max_length=30, blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sue_consolidado'


class SueCostero(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=150, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.CharField(max_length=254, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.CharField(max_length=30, blank=True, null=True)
    igds_weigh = models.CharField(max_length=30, blank=True, null=True)
    rotation = models.CharField(max_length=30, blank=True, null=True)
    igds_color = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)
    igds_level = models.CharField(max_length=30, blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sue_costero'


class SueHidromorfologico(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=112, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.CharField(max_length=30, blank=True, null=True)
    igds_weigh = models.CharField(max_length=30, blank=True, null=True)
    rotation = models.CharField(max_length=30, blank=True, null=True)
    igds_color = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)
    igds_level = models.CharField(max_length=30, blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sue_hidromorfologico'


class SueNoConsolidado(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=84, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.CharField(max_length=30, blank=True, null=True)
    igds_weigh = models.CharField(max_length=30, blank=True, null=True)
    rotation = models.CharField(max_length=30, blank=True, null=True)
    igds_color = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)
    igds_level = models.CharField(max_length=30, blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sue_no_consolidado'


class VegArborea(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=107, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'veg_arborea'


class VegArbustiva(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'veg_arbustiva'


class VegCultivos(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=47, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.CharField(max_length=30, blank=True, null=True)
    igds_type = models.CharField(max_length=30, blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'veg_cultivos'


class VegHidrofila(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=192, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    opeador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'veg_hidrofila'


class VegSueloDesnudo(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=70, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    detalle = models.CharField(max_length=254, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'veg_suelo_desnudo'


class ViasSecundarias(models.Model):
    gid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=91, blank=True, null=True)
    precisión = models.CharField(max_length=29, blank=True, null=True)
    escala = models.CharField(max_length=61, blank=True, null=True)
    signo = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=50, blank=True, null=True)
    dataset = models.CharField(max_length=77, blank=True, null=True)
    fclass = models.CharField(max_length=75, blank=True, null=True)
    responsabl = models.CharField(max_length=30, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    progreso = models.CharField(max_length=20, blank=True, null=True)
    t_act = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=50, blank=True, null=True)
    sp = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=10, blank=True, null=True)
    ac = models.CharField(max_length=4, blank=True, null=True)
    material = models.CharField(max_length=29, blank=True, null=True)
    actualizac = models.CharField(max_length=20, blank=True, null=True)
    uso = models.CharField(max_length=29, blank=True, null=True)
    igds_style = models.FloatField(blank=True, null=True)
    igds_type = models.FloatField(blank=True, null=True)
    igds_weigh = models.FloatField(blank=True, null=True)
    rotation = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    igds_color = models.FloatField(blank=True, null=True)
    group = models.FloatField(blank=True, null=True)
    igds_level = models.FloatField(blank=True, null=True)
    length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vias_secundarias'
