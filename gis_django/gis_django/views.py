from django.shortcuts import render
from osgeo import ogr
import mapnik, os


def index(request):
    m = mapnik.Map(700, 700)
    m.background = mapnik.Color("white")
    

    polygons = mapnik.PolygonSymbolizer()
    polygons.fill = mapnik.Color("orange")

    rules = mapnik.Rule()
    rules.symbols.append(polygons)

    style = mapnik.Style()
    style.rules.append(rules)

    # Creating rules 
    highlight = mapnik.PolygonSymbolizer()

    highlight.fill = mapnik.Color('red')
    r = mapnik.Rule()
    r.filter = mapnik.Expression("[productivi] <= 31")
    r.symbols.append(highlight)
    style.rules.append(r)

    highlight.fill = mapnik.Color('green')
    g = mapnik.Rule()
    g.filter = mapnik.Expression("[productivi] >= 70")
    g.symbols.append(highlight)
    style.rules.append(g)


    m.append_style('Polygons', style)

    layer = mapnik.Layer('A')

    layer.datasource = mapnik.PostGIS(host='127.0.0.1',user='eugene', \
                                        password='88888888',dbname='geotest', \
                                        table='map_map', srid='3857')
    layer.styles.append('Polygons')
    m.layers.append(layer)


    rules.symbols.append(polygons)
    style.rules.append(rules)

    m.zoom_all()
    mapnik.render_to_file(m, os.path.abspath('FileStorage/polygons.png'), 'png')
    
    return render(request, 'base.html')
    
