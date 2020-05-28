# -*- coding: utf-8 -*-


from didicloud.sdk.base.v1.base_pb2 import Error,Header,ZoneInfo,RegionInfo,JobInfo,RegionAndZoneInfo
from didicloud.sdk.bill.v1.bill_pb2 import Dc2Spec,EipSpec,EbsSpec,ResourceSpec,ChargeInfo,FactorRuleDetail,BuyDetail,FactorRuleFilter,ContinueListCondition,ContinueListRequest,ResourceItemOutput,ContinueListItem,ContinueListResponse,ResourceItemInput,ContinueMonthlyRequest,ContinueMonthlyResponse,ChangeToMonthlyRequest,ChangeToMonthlyResponse,ChangeExpireStrategyRequest,ChangeExpireStrategyResponse,CheckDc2PriceInput,CheckEipPriceInput,CheckEbsPriceInput,CheckDc2PriceRequest,CheckEipPriceRequest,CheckEbsPriceRequest,CheckPriceInfo,CheckPriceResponse,GetChargeInfoInput,GetChargeInfoAndSpecRequest,Dc2ChargeInfoAndSpec,EipChargeInfoAndSpec,EbsChargeInfoAndSpec,GetDc2ChargeInfoAndSpecResponse,GetEipChargeInfoAndSpecResponse,GetEbsChargeInfoAndSpecResponse
from didicloud.sdk.compute.v1.common_pb2 import Dc2Info,EipInfo,EbsInfo,SnapInfo,VpcInfo,SubnetInfo,TotalCntInfo,SgInfo,SgRuleInfo,JobResultRequest,JobResultResponse,ListRegionAndZoneRequest,RegionData,ListRegionAndZoneResponse
from didicloud.sdk.compute.v1.dc2_pb2 import ListDc2Response,ListDc2Condition,ListDc2Request,GetDc2TotalCntRequest,GetDc2TotalCntResponse,GetDc2ByUuidRequest,GetDc2ByUuidResponse,ChangeDc2SpecRequest,ChangeDc2SpecResponse,ReinstallDc2SystemRequest,ReinstallDc2SystemResponse,DestroyDc2Request,DestroyDc2Response,StartDc2Request,StartDc2Response,StopDc2Request,StopDc2Response,RebootDc2Request,RebootDc2Response,ChangeDc2NameRequest,ChangeDc2NameResponse,ChangeDc2PasswordRequest,ChangeDc2PasswordResponse,CreateDc2Request,CreateDc2Response,ListImageRequest,ListImageResponse,SshKey,ListSshKeyRequest,ListSshKeyResponse,CreateSshKeyRequest,CreateSshKeyResponse,DeleteSshKeyRequest,DeleteSshKeyResponse
from didicloud.sdk.compute.v1.eip_pb2 import ListEipResponse,ListEipCondition,ListEipRequest,GetEipTotalCntRequest,GetEipTotalCntResponse,GetEipByUuidRequest,GetEipByUuidResponse,CreateEipRequest,CreateEipResponse,ChangeEipBandwidthRequest,ChangeEipBandwidthResponse,DeleteEipRequest,DeleteEipResponse,AttachEipToDc2Request,AttachEipToDc2Response,DetachEipFromDc2Request,DetachEipFromDc2Response
from didicloud.sdk.compute.v1.ebs_pb2 import ListEbsRequest,ListEbsCondition,ListEbsResponse,GetEbsByUuidRequest,GetEbsByUuidResponse,GetEbsTotalCntRequest,GetEbsTotalCntResponse,CreateEbsRequest,CreateEbsResponse,DeleteEbsRequest,DeleteEbsResponse,AttachEbsRequest,AttachEbsResponse,DetachEbsRequest,DetachEbsResponse,ChangeEbsSizeRequest,ChangeEbsSizeResponse,ChangeEbsNameRequest,ChangeEbsNameResponse
from didicloud.sdk.compute.v1.sg_pb2 import ListSgResponse,ListSgCondition,ListSgRequest,GetSgTotalCntRequest,GetSgTotalCntResponse,CreateSgRuleInput,CreateSgRequest,CreateSgResponse,DeleteSgRequest,DeleteSgResponse,ChangeSgNameRequest,ChangeSgNameResponse,AttachDc2ToSgRequest,AttachDc2ToSgResponse,DetachDc2FromSgRequest,DetachDc2FromSgResponse,ListSgRuleCondition,ListSgRuleRequest,ListSgRuleResponse,GetSgRuleTotalCntRequest,GetSgRuleTotalCntResponse,CreateSgRuleRequest,CreateSgRuleResponse,DeleteSgRuleRequest,DeleteSgRuleResponse
from didicloud.sdk.compute.v1.snap_pb2 import ListSnapshotRequest,ListSnapshotCondition,ListSnapshotResponse,GetSnapshotTotalCntRequest,GetSnapshotTotalCntResponse,CreateSnapshotRequest,CreateSnapshotResponse,DeleteSnapshotRequest,DeleteSnapshotResponse,RevertSnapshotRequest,RevertSnapshotResponse,ChangeSnapshotNameRequest,ChangeSnapshotNameResponse
from didicloud.sdk.compute.v1.vpc_pb2 import ListVpcRequest,ListVpcResponse,GetVpcByUuidRequest,GetVpcByUuidResponse,GetVpcTotalCntRequest,GetVpcTotalCntResponse,CreateSubnetInput,CreateVpcRequest,CreateVpcResponse,DeleteVpcRequest,DeleteVpcResponse,ChangeVpcNameRequest,ChangeVpcNameResponse,ListVpcAvailableCidrRequest,VpcAvailableCidr,ListVpcAvailableCidrResponse,ListSubnetRequest,ListSubnetCondition,ListSubnetResponse,GetSubnetByUuidRequest,GetSubnetByUuidResponse,GetSubnetTotalCntRequest,GetSubnetTotalCntResponse,CreateSubnetRequest,CreateSubnetResponse,DeleteSubnetRequest,DeleteSubnetResponse,ChangeSubnetNameRequest,ChangeSubnetNameResponse,CheckSubnetCidrOverlapRequest,CheckSubnetCidrOverlapResponse,IsOverlapOutput
from didicloud.sdk.monitor.v1.counter_pb2 import ListCounterRequest,CounterResource,ListCounterResponse,CounterOutput,CounterInfo,ListCounterDataRequest,CounterDataInput,ListCounterDataResponse,CounterDataOutput,CounterDataValue
