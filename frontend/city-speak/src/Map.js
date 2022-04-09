import React, { useEffect, useState } from "react";
import { Map, Marker } from "pigeon-maps";
import { stamenToner } from 'pigeon-maps/providers'

import Geocode from "react-geocode";

const MyMap = () => {

  const [center, setCenter] = useState([48.85837009999999, 2.2944813]);

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
      center={center}
      defaultZoom={4}
    >
      <Marker width={50} anchor={center} />
    </Map>
  );
};

export default MyMap;
