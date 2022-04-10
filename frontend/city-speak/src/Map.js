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
            ? { fill: '#93c0d099', strokeWidth: '2'}
            : { fill: '#d4e6ec99', strokeWidth: '1'}
        }
      />

      <Marker width={50} anchor={props.center} />
    </Map>
  );
};

export default MyMap;
