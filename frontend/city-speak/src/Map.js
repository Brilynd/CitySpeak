import React, { useEffect, useState } from "react";
import { Map, Marker } from "pigeon-maps";
import { stamenToner } from 'pigeon-maps/providers'

import Geocode from "react-geocode";

const MyMap = (props) => {

  // useEffect(() => {
  //   Geocode.setApiKey("AIzaSyDgKlIduRn5Dvn6UBVwmoFpdQsFKNdpWQY");
  //   Geocode.setLanguage("en");

  //   // Get latitude & longitude from address.
  //   Geocode.fromAddress("Eiffel Tower").then(
  //     (response) => {
  //       const { lat, lng } = response.results[0].geometry.location;
  //       setCenter([lat, lng] );
  //       console.log(lat, lng);
  //     },
  //     (error) => {
  //       console.error(error);
  //     }
  //   );
  // }, [])

  return (
    <Map
      provider={stamenToner}
      center={props.center}
      defaultZoom={4}
    >
      <Marker width={50} anchor={props.center} />
    </Map>
  );
};

export default MyMap;
