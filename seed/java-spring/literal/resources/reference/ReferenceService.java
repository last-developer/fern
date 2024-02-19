/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.reference;

import java.lang.Boolean;
import java.lang.String;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import resources.reference.types.SendRequest;
import types.SendResponse;

@RequestMapping(
    path = "/"
)
public interface ReferenceService {
  @PostMapping(
      value = "/reference",
      produces = "application/json",
      consumes = "application/json"
  )
  SendResponse send(@RequestHeader("X-API-Version") String version,
      @RequestHeader("X-API-Enable-Audit-Logging") Boolean auditLogging,
      @RequestBody SendRequest body);
}
