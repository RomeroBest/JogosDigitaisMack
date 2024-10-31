/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/WebServices/GenericResource.java to edit this template
 */
package WS;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.MediaType;

/**
 * REST Web Service
 *
 * @author jorja
 */
@Path("principal")
public class principal {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of principal
     */
    public principal() {
    }

    /**
     * Retrieves representation of an instance of WS.principal
     * @param N1
     * @param N2
     * @return an instance of java.lang.String
     */
    //@GET
    //@Produces(MediaType.TEXT_PLAIN)
    //public String getText() {
        //TODO return proper representation object
        //throw new UnsupportedOperationException();
    //    return "Web Service RESTful - Olá Mundo !!";
    //}
    
    @GET
    @Produces(javax.ws.rs.core.MediaType.TEXT_PLAIN)
    @Path("Potência/{N1}/{N2}")
    public String getPotencia(@PathParam("N1") int N1, @PathParam("N2") int N2) {
        double resp= Math.pow(N1,N2);
        return "Potencia: "+N1+ "^" +N2+ " igual a "+ resp;
    }
    
    

    /**
     * PUT method for updating or creating an instance of principal
     * @param content representation for the resource
     */
    @PUT
    @Consumes(MediaType.TEXT_PLAIN)
    public void putText(String content) {
    }
}
