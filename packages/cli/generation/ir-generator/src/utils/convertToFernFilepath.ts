import { dirname, RelativeFilePath } from "@fern-api/fs-utils";
import { FERN_PACKAGE_MARKER_FILENAME } from "@fern-api/project-configuration";
import { FernFilepath } from "@fern-fern/ir-model/commons";
import path, { basename } from "path";
import { CasingsGenerator } from "../casings/CasingsGenerator";

export function convertToFernFilepath({
    relativeFilepath,
    casingsGenerator,
}: {
    relativeFilepath: RelativeFilePath;
    casingsGenerator: CasingsGenerator;
}): FernFilepath {
    const pathToPackage = dirname(relativeFilepath);
    const filename = basename(relativeFilepath);
    return {
        packagePath:
            pathToPackage === "."
                ? []
                : pathToPackage.split(path.sep).map((part) => casingsGenerator.generateName(part)),
        file:
            filename !== FERN_PACKAGE_MARKER_FILENAME
                ? casingsGenerator.generateName(path.parse(filename).name)
                : undefined,
    };
}
