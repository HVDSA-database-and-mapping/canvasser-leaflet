L.GridLayer.GeoJSON = L.GridLayer.extend({
      options: {
              minZoom: 0,
              maxZoom: 18,
              subdomains: 'abc',
              zoomReverse: false,
              zoomOffset: 0
            },
      initialize: function(url, options) {

              this._url = url;

              options = L.Util.setOptions(this, options);

              if (typeof options.subdomains === 'string') {
                        options.subdomains = options.subdomains.split('');
                      }

              this.on('tileunload', function(event) {
                        event.tile.layer && event.tile.layer.remove();
                      });
            },
      getTileUrl: L.TileLayer.prototype.getTileUrl,
      _getSubdomain: L.TileLayer.prototype._getSubdomain,
      _getZoomForUrl: L.TileLayer.prototype._getZoomForUrl,
      _xhrHandler: function(req, layer, tile, tilePoint, done) {
              return function() {
                        if (req.readyState !== 4) {
                                    return;
                                  }
                        var s = req.status;
                        if ((s >= 200 && s < 300 && s != 204) || s === 304) {
                                    tile.datum = JSON.parse(req.responseText);
                                    tile.layer = L.geoJSON(tile.datum.roads).addTo(map);
                                    done();
                                  }
                      };
            },
      createTile: function(coords, done) {
              var tile = document.createElement('div');
              var layer = this;
              var req = new XMLHttpRequest();
              req.onreadystatechange = this._xhrHandler(req, layer, tile, coords, done);
              req.open('GET', this.getTileUrl(coords), true);
              req.send();
              return tile;
            }
});
