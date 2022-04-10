import React, { useEffect, useState } from "react";
import { Map, Marker, GeoJsonLoader } from "pigeon-maps";
import { stamenTerrain  } from 'pigeon-maps/providers'

import Geocode from "react-geocode";

const MyMap = (props) => {

  const geoJsonLink = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"



  return (
    <Map
      provider={stamenTerrain}
      center={props.center}
      defaultZoom={4}
      maxZoom={7}
    >
      <GeoJsonLoader
        link={geoJsonLink}
        styleCallback={(feature, hover) =>
          hover
            ? { fill: '#A7EFE999', strokeWidth: '2'}
            : { fill: '#d4e6ec00', strokeWidth: '1'}
        }
        onClick={(e => {
          let coords = e.payload.geometry.coordinates;
          // deal with when state is in multiple polygons
          if (coords.length > 1) {
            coords = coords[0];
          }
          console.log(coords)
          const avgLat = coords[0].map(coord => coord[0]).reduce((a, b) => a + b) / coords[0].length;
          const avgLon = coords[0].map(coord => coord[1]).reduce((a, b) => a + b) / coords[0].length;
          
          props.onLocationChange(e.payload.properties.name, [avgLon, avgLat]);
        })}
      />

      <Marker width={50} anchor={props.center} />
    </Map>
  );
};

export default MyMap;
