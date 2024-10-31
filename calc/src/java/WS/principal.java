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
@Path("principal") //este caminho pode ser retirado para que o calculo seja feito diretamente no URL. 
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
     * @param n1
     * @param n2
     * @return an instance of java.lang.String
     */
    @GET
    @Path("/add/{n1}/{n2}")
    @Produces(MediaType.TEXT_HTML)
    public String add(@PathParam("n1") int n1, @PathParam("n2") int n2) {
        int result = n1 + n2;
        return "<p>" + n1 + " + " + n2 + " = " + result + "</p>";
    }

    @GET
    @Path("/sub/{n1}/{n2}")
    @Produces(MediaType.TEXT_HTML)
    public String subtract(@PathParam("n1") int n1, @PathParam("n2") int n2) {
        int result = n1 - n2;
        return "<p>" + n1 + " - " + n2 + " = " + result + "</p>";
    }

    @GET
    @Path("/mul/{n1}/{n2}")
    @Produces(MediaType.TEXT_HTML)
    public String multiply(@PathParam("n1") int n1, @PathParam("n2") int n2) {
        int result = n1 * n2;
        return "<p>" + n1 + " * " + n2 + " = " + result + "</p>";
    }

    @GET
    @Path("/div/{n1}/{n2}")
    @Produces(MediaType.TEXT_HTML)
    public String divide(@PathParam("n1") int n1, @PathParam("n2") int n2) {
        if (n2 == 0) {
            return "<p>Erro: divisão por zero.</p>";
        }
        int result = n1 / n2;
        return "<p>" + n1 + " / " + n2 + " = " + result + "</p>";
    }

    @GET
    @Path("/pow/{n1}/{n2}")
    @Produces(MediaType.TEXT_HTML)
    public String power(@PathParam("n1") int n1, @PathParam("n2") int n2) {
        int result = (int) Math.pow(n1, n2);
        return "<p>" + n1 + " ^ " + n2 + " = " + result + "</p>";
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
