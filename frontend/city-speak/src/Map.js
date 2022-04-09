import React from "react";
import { Map, Marker } from "pigeon-maps";
import { stamenToner } from 'pigeon-maps/providers'

const MyMap = () => {
  return (
    <Map
      provider={stamenToner}
      height={300}
      defaultCenter={[50.879, 4.6997]}
      defaultZoom={11}
    >
      <Marker width={50} anchor={[50.879, 4.6997]} />
    </Map>
  );
};

export default MyMap;
