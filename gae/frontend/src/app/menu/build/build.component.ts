/**
 * Copyright (C) 2018 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import { Component } from '@angular/core';
import { MatTableDataSource, PageEvent } from '@angular/material';

import { Build } from '../../model/build';
import { BuildService } from './build.service';
import { MenuBaseClass } from '../menu_base';


@Component({
  selector: 'app-build',
  templateUrl: './build.component.html',
  providers: [ BuildService ],
  styleUrls: ['./build.component.scss'],
})
export class BuildComponent extends MenuBaseClass {
  columnTitles = [
    '_index',
    'artifact_type',
    'build_id',
    'build_target',
    'build_type',
    'manifest_branch',
    'signed'];
  dataSource = new MatTableDataSource<Build>();
  pageEvent: PageEvent;

  constructor(private buildService: BuildService) {
    super();
  }

  onPageEvent(event: PageEvent) {
    this.pageSize = event.pageSize;
    this.pageIndex = event.pageIndex;
    return event;
  }
}
