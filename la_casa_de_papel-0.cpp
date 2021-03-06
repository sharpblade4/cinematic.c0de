/*
  La Casa de Papel (/ Money Heist) - s03e02 03:01 
  
  Potential Source:
   -  https://github.com/BCN3D/BCN3D-Moveo/blob/master/FIRMWARE/Marlin_BCN3D_Moveo/Marlin_main.cpp
*/

    case 31: // dock the sled
        dock_sled(true);
        break;
    case 32: // undock the sled
        dock_sled(false);
        break;
#endif // Z_PROBE_SLED
#endif // ENABLE_AUTO_BED_LEVELING
    case 90: // G90
      relative_mode = false;
      break;
    case 91: // G91
      relative_mode = true;
      break;
    case 92: // G92
      if(!code_seen(axis_codes[E_AXIS]))
        st_synchronize();
      for(int8_t i=0; i < NUM_AXIS; i++) {
